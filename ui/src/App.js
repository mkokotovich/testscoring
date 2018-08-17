import React, { Component } from 'react';
import { Row, Col } from 'antd';
import logo from './logo.svg';
import './App.css';
import SignIn from './SignIn';
import Home from './Home';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null
    };
  }

  handleAuthChange = (user) => {
    this.setState({
      user: user,
    });
  }

  render() {
    return (
      <div className="App">
        <Row
          type="flex"
          justify="space-between"
          className="navbar"
          align="middle"
          >
          <Col className="Logo">Test Scoring</Col>
          <Col><SignIn handleAuthChange={this.handleAuthChange} /></Col>
        </Row>
        <Home signedInUser={this.state.user} />
      </div>
    );
  }
}

export default App;
