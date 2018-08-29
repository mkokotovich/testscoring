import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Modal, Spin, Affix, Button } from 'antd';
import axios from 'axios';
import ItemList from './ItemList';
import './TestEdit.css';

class TestEdit extends Component {
  state = {
    test: {},
    readonly: false,
    loading: false,
    conflicts: {}
  }

  componentDidMount() {
    this.loadTest();
    if (this.props.location.state) {
      const {readonly} = this.props.location.state
      if (readonly) {
        this.setState({readonly})
      }
    }
    if (this.props.readonly !== undefined) {
      this.setState({readonly: this.props.readonly})
    }
    
  }

  componentDidUpdate(prevProps) {
    if (this.props.match.params.testId !== prevProps.match.params.testId) {
      this.setState({test: []});
      this.loadTest();
    }
  }

  loadTest = () => {
    this.setState({loading: true});
    axios.get(`/api/testing/v1/tests/${this.props.match.params.testId}/`)
      .then((response) => {
        console.log(response);
        this.setState({
          loading: false,
          test: response.data
        });
      })
      .catch((error) => {
        console.log(error);
        this.setState({loading: false});
        Modal.error({
          title: "Unable to load test",
          content: "Unable to load test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  updateConflicts = (itemId, conflict) => {
    var newConflicts = this.state.conflicts;
    newConflicts[itemId] = conflict;
    this.setState({ conflicts: newConflicts });
  }

  handleEdit = () => {
    const testId = this.props.match.params.testId;
    this.props.history.push(`/tests/${testId}/edit`)
  }

  handleVerify = () => {
    const testId = this.props.match.params.testId;
    this.props.history.push(`/tests/${testId}/verify`)
  }

  handleViewInconsistencies = () => {
    const onlyErrors = Object.keys(this.state.conflicts).reduce((filtered, key) => {
      if (this.state.conflicts[key]) {
        filtered.push(key);
      }
      return filtered;
    }, []);
    if (onlyErrors.length > 0) {
      Modal.error({
        title: "Inconsistencies Found",
        content: "Inconsistencies found in items " + onlyErrors.join(", "),
        maskClosable: true,
      })
    }
  }

  handleViewScores = () => {
    const testId = this.props.match.params.testId;
    this.props.history.push(`/tests/${testId}/scores`)
  }

  render() {
    const testId = this.props.match.params.testId;
    const allVerified = this.state.test.items ? Object.keys(this.state.conflicts).length === this.state.test.items.length : false;
    const inconsistencies = Object.keys(this.state.conflicts).reduce((filtered, key) => {
      if (this.state.conflicts[key]) {
        filtered.push(key);
      }
      return filtered;
    }, []);

    return (
      <div className="TestEdit">
        <h2>Test {testId}: {this.state.test.test_type} for client {this.state.test.client_number}</h2>
        <div align="center">
          { this.state.loading && <Spin size="large" />}
        </div>

        <Affix>
          <div className="AlignRight">
            { this.state.readonly ? 
              <Button
                className="TopRightButton"
                onClick={this.handleEdit}>
                  Edit
              </Button> : '' 
            }
            { this.props.verify ? (
              <React.Fragment>
              { inconsistencies.length > 0 ? 
                <Button
                  className="TopRightButton"
                  onClick={this.handleViewInconsistencies}>
                    View Inconsistencies
                </Button> : ''
              }
              {
                allVerified && inconsistencies.length === 0 ? 
                <Button
                  className="TopRightButton"
                  onClick={this.handleViewScores}>
                    View Scores
                </Button> : ''
              }
              </React.Fragment>
            ) :
              <React.Fragment>
                <Button
                  className="TopRightButton"
                  onClick={this.handleVerify}>
                    Verify
                </Button>
                <Button
                  className="TopRightButton"
                  onClick={this.handleViewScores}>
                    View Scores
                </Button>
              </React.Fragment>
            }
          </div>
        </Affix>

        <ItemList
          items={this.state.test.items}
          readonly={this.state.readonly}
          verify={this.props.verify}
          updateConflicts={this.updateConflicts}
        />
      </div>
    );
  }
}

export default withRouter(TestEdit);
