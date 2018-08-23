import React, { Component } from 'react';
import { Route, Link, withRouter } from 'react-router-dom';
import { Row, Col, Spin } from 'antd';
import { Input, Card, Modal, Button } from 'antd';
import axios from 'axios';
import './Home.css';

class Home extends Component {

  state = {
    visible: false,
    clientID: undefined,
    loading: false
  }

  showModal = () => {
    this.setState({
      visible: true,
    });
  }

  viewExisting = () => {
    this.props.history.push('/tests/cbcl_6_18/');
  }

  handleOk = (e) => {
    this.setState({
      loading: true
    });
    var test_data = {
      client_number: this.state.clientID,
      test_type: "cbcl_6_18"
    }
    axios.post('/api/testing/v1/tests/', test_data)
      .then((response) => {
        console.log(response);
        this.setState({
          loading: false,
          visible: false
        });
        this.props.history.push(`/tests/${response.data.id}/edit`);
      })
      .catch((error) => {
        console.log(error);
        this.setState({
          loading: false,
          visible: false
        });
        Modal.error({
          title: "Unable to start a new scoring",
          content: "Unable to start a new scoring. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  handleCancel = (e) => {
    this.setState({
      visible: false,
    });
  }

  onChangeClientID = (e) => {
    this.setState({ clientID: e.target.value });
  }

  render() {
    if (!this.props.signedInUser) {
      return (
        <div>
          Sign in to continue
        </div>
      );
    }
    return (
      <div className="Home">
        <Card style={{ width: 350 }}>
          <h1>CBCL 6-18</h1>
          <div align="right">
            <Button type="primary" onClick={this.showModal}>Start New</Button>
            &nbsp;
            <Button type="primary" onClick={this.viewExisting}>View Existing</Button>
          </div>
          <Modal
            title="Start a new CBCL 6-18 scoring"
            visible={this.state.visible}
            onOk={this.handleOk}
            okText="Start"
            okButtonProps={{ disabled: !this.state.clientID }}
            onCancel={this.handleCancel}
          >
            <div align="center">
              { this.state.loading && <Spin size="large" />}
            </div>
            <p>Please enter the client ID</p>
            <Input
              placeholder="Enter Client ID"
              value={this.state.clientID}
              onChange={this.onChangeClientID}
            />
          </Modal>
        </Card>
      </div>
    );
  }
}

export default withRouter(Home);
