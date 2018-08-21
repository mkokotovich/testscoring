import React, { Component } from 'react';
import { Route, Link, withRouter } from 'react-router-dom';
import { Row, Col } from 'antd';
import { Input, Card, Modal, Button } from 'antd';
import './Home.css';

class Home extends Component {

  state = {
    visible: false,
    clientID: undefined
  }

  showModal = () => {
    this.setState({
      visible: true,
    });
  }

  viewExisting = () => {
    this.props.history.push('/cbcl-list');
  }

  handleOk = (e) => {
    this.setState({
      visible: false,
    });
    this.props.history.push('/cbcl-new');
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
    return (
      <div className="Home">
        <Card style={{ width: 350 }}>
          <h1>CBCL</h1>
          <div align="right">
            <Button type="primary" onClick={this.showModal}>Start New</Button>
            &nbsp;
            <Button type="primary" onClick={this.viewExisting}>View Existing</Button>
          </div>
          <Modal
            title="Start a new CBCL scoring"
            visible={this.state.visible}
            onOk={this.handleOk}
            okText="Start"
            okButtonProps={{ disabled: !this.state.clientID }}
            onCancel={this.handleCancel}
          >
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
