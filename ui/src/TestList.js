import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Button, Modal, Spin, Divider } from 'antd';
import Test from './Test';
import Search from './Search';
import axios from 'axios';
import queryString from 'query-string';
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
    if (this.props.location.search !== prevProps.location.search) {
      this.setState({tests: []});
      this.loadTests();
    }
  }

  loadTests = () => {
    this.setState({loading: true});
    const values = queryString.parse(this.props.location.search)
    var query = "";
    var sep = "?";
    if (values.type) {
      query = `${query}${sep}test_type=${values.type}`;
      sep = "&";
    }
    if (values.search) {
      query = `${query}${sep}search=${values.search}`;
      sep = "&";
    }
    if (values.clientid) {
      query = `${query}${sep}client_number=${values.clientid}`;
      sep = "&";
    }
    axios.get(`/api/testing/v1/tests/${query}`)
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

  updateStateWithNewTest = (newTest) => {
    const updatedTests = this.state.tests.map((test) => {
      if (test.id === newTest.id) {
        return newTest;
      } else {
        return test;
      }
    });
    this.setState({ tests: updatedTests });
  }

  handleArchiveAll = () => {
    console.log("archiving all tests");
    axios.post(`/api/testing/v1/tests/archiveall/`)
      .then((response) => {
        console.log(response);
        const newTests = response.data;
        this.setState({ tests: newTests });
      })
      .catch((error) => {
        console.log(error);
        Modal.error({
          title: "Unable to archive all tests",
          content: "Unable to archive all tests. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  handleArchive = (testId) => {
    console.log("archive " + testId);
    axios.post(`/api/testing/v1/tests/${testId}/archive/`)
      .then((response) => {
        console.log(response);
        const newTest = response.data;
        this.updateStateWithNewTest(newTest);
      })
      .catch((error) => {
        console.log(error);
        Modal.error({
          title: "Unable to archive test",
          content: "Unable to archive test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  handleRestore = (testId) => {
    console.log("restore " + testId);
    axios.post(`/api/testing/v1/tests/${testId}/restore/`)
      .then((response) => {
        console.log(response);
        const newTest = response.data;
        this.updateStateWithNewTest(newTest);
      })
      .catch((error) => {
        console.log(error);
        Modal.error({
          title: "Unable to restore test",
          content: "Unable to restore test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
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
        <Test
          test={test}
          handleArchive={this.handleArchive}
          handleRestore={this.handleRestore}
          handleDelete={this.handleDelete}
          assessmentBySlug={this.props.assessmentBySlug}
        />
        <Divider />
      </div>
    );
    return (
      <div className="TestList">
        <Search/>
        <div align="center">
          { this.state.loading && <Spin size="large" />}
        </div>
        <Divider />
        {tests}
        <Button onClick={this.handleArchiveAll}>Archive All Tests</Button>
      </div>
    );
  }
}

export default withRouter(TestList);
