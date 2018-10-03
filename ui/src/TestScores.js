import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Modal, Spin } from 'antd';
import axios from 'axios';
import ScoreList from './ScoreList';
import './TestScores.css';

class TestScores extends Component {
  state = {
    testScores: {},
    loading: false
  }

  componentDidMount() {
    this.loadScores();
  }

  componentDidUpdate(prevProps) {
    if (this.props.match.params.testId !== prevProps.match.params.testId) {
      this.setState({testScores: {}});
      this.loadScores();
    }
  }

  loadScores = () => {
    this.setState({loading: true});
    axios.get(`/api/testing/v1/tests/${this.props.match.params.testId}/scores`)
      .then((response) => {
        console.log(response);
        this.setState({
          loading: false,
          testScores: response.data
        });
      })
      .catch((error) => {
        console.log(error);
        this.setState({loading: false});
        Modal.error({
          title: "Unable to load scores",
          content: "Unable to load scores:\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  render() {
    const testId = this.props.match.params.testId;
    return (
      <div className="TestScores">
        { this.state.testScores.test && <h2>Scores for {this.state.testScores.test.test_type} for client {this.state.testScores.test.client_number}</h2> }
        <div align="center">
          { this.state.loading && <Spin size="large" />}
        </div>

        <ScoreList scores={this.state.testScores.scores} test={this.state.testScores.test} />
      </div>
    );
  }
}

export default withRouter(TestScores);
