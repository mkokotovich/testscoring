import React, { Component } from 'react';
import { Route, Link } from 'react-router-dom';
import { Modal, Row, Col } from 'antd';
import axios from 'axios';
import './App.css';
import SignIn from './SignIn';
import Home from './Home';
import TestEdit from './TestEdit';
import TestList from './TestList';
import TestScores from './TestScores';
import Profile from './Profile';
import ChangePassword from './ChangePassword';
import ForgotPassword from './ForgotPassword';
import ResetPassword from './ResetPassword';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      user: null,
      assessmentBySlug: {},
    };
  }

  setAssessmentBySlug = (abs) => {
    this.setState({assessmentBySlug: abs});
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
          <Col className="Logo"><Link to="/">Test Scoring</Link></Col>
        </Row>
        <br />
        <h2>This URL is being shut down. Please use this site through <a href="https://testscoring.fly.dev">https://testscoring.fly.dev</a></h2>
      </div>
    );
  }
}

export default App;
