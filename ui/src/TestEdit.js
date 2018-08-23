import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col, Modal, Input, Spin } from 'antd';
import axios from 'axios';
import ItemList from './ItemList';
import './TestEdit.css';

class TestEdit extends Component {
  state = {
    test: {},
    loading: false
  }

  componentDidMount() {
    this.loadTest();
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

  render() {
    const testId = this.props.match.params.testId;
    return (
      <div className="TestEdit">
        <h2>Test {testId}: {this.state.test.test_type} for client {this.state.test.client_number}</h2>
        <div align="center">
          { this.state.loading && <Spin size="large" />}
        </div>
        <ItemList items={this.state.test.items} />
      </div>
    );
  }
}

export default withRouter(TestEdit);
