import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col, Modal } from 'antd';
import axios from 'axios';
import './TestEdit.css';

class TestEdit extends Component {
  state = {
    test: {},
    loading: false
  }

  componentDidMount() {
    this.loadTest();
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

  render() {
    const testId = this.props.match.params.testId;
    return (
      <div className="TestEdit">
        Edit test {testId}
        <br/><br/>
        <pre>
        {JSON.stringify(this.state.test, undefined, 2)}
        </pre>
      </div>
    );
  }
}

export default withRouter(TestEdit);
