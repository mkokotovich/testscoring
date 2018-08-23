import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col, Modal, Spin } from 'antd';
import axios from 'axios';
import TestSummary from './TestSummary';
import './TestList.css';

class TestList extends Component {
  state = {
    tests: [],
    loading: false
  }

  componentDidMount() {
    this.loadTests();
  }

  loadTests = () => {
    this.setState({loading: true});
    const testType = this.props.match.params.testType;
    axios.get(`/api/testing/v1/tests/?test_type=${testType}`)
      .then((response) => {
        console.log(response);
        this.setState({
          loading: false,
          tests: response.data
        });
      })
      .catch((error) => {
        console.log(error);
        this.setState({loading: false});
        Modal.error({
          title: "Unable to load tests",
          content: "Unable to load tests. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  render() {
    var summary = this.state.tests.map(test =>
      <TestSummary test={test} />
    );
    return (
      <div className="TestList">
        <h2>All Tests</h2>
        <div align="center">
          { this.state.loading && <Spin size="large" />}
        </div>
        {summary}
      </div>
    );
  }
}

export default withRouter(TestList);
