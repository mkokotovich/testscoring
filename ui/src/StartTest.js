import React, { Component } from 'react';
import { withRouter} from 'react-router-dom';
import { Card, Button, Modal, Spin, Input } from 'antd';
import axios from 'axios';
import './StartTest.css';

class StartTest extends Component {
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
    this.props.history.push(`/tests/?type=${this.props.assessment.slug}`);
  }

  handleOk = (e) => {
    this.setState({
      loading: true
    });
    var test_data = {
      client_number: this.state.clientID,
      test_type: this.props.assessment.slug
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


  componentDidMount() {
  }

  render() {

    return (
      <div className="StartTest">
        <Card style={{ width: 350 }}>
          <h1>{this.props.assessment.name}</h1>
          <div align="right">
            <Button type="primary" onClick={this.showModal}>Start New</Button>
            &nbsp;
            <Button type="primary" onClick={this.viewExisting}>View Existing</Button>
          </div>
          <Modal
            title={"Start a new " + this.props.assessment.name + " scoring"}
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
              onPressEnter={() => this.handleOk()}
            />
          </Modal>
        </Card>
      </div>
    );
  }
}

export default withRouter(StartTest);
