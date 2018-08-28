import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Modal, Spin, Divider } from 'antd';
import Test from './Test';
import axios from 'axios';
import './TestList.css';

class TestList extends Component {
  state = {
    tests: [],
    loading: false
  }

  componentDidMount() {
    this.loadTests();
  }

  componentDidUpdate(prevProps) {
    if (this.props.match.params.testType !== prevProps.match.params.testType) {
      this.setState({tests: []});
      this.loadTests();
    }
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

  handleDelete = (testId) => {
    console.log("delete " + testId);
    axios.delete(`/api/testing/v1/tests/${testId}/`)
      .then((response) => {
        console.log(response);
        const tests = [...this.state.tests];
        this.setState({ tests: tests.filter(item => item.id !== testId) });
      })
      .catch((error) => {
        console.log(error);
        Modal.error({
          title: "Unable to delete test",
          content: "Unable to delete test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  expandedRowRender = (record) => {
    return (
      <div>
        Created at: {record.created_at} and last modified at: {record.updated_at}
      </div>
    )
  }

  render() {
    const tests = this.state.tests.map(test =>
      <div key={test.id}>
        <Test test={test} handleDelete={this.handleDelete} />
        <Divider />
      </div>
    );
    return (
      <div className="TestList">
        <h2>All {this.props.match.params.testType} Tests</h2>
        <div align="center">
          { this.state.loading && <Spin size="large" />}
        </div>
        <Divider />
        {tests}
      </div>
    );
  }
}

export default withRouter(TestList);
