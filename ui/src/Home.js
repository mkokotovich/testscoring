import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Row, Modal, Spin } from 'antd';
import StartTest from './StartTest';
import Search from './Search';
import axios from 'axios';
import './Home.css';

class Home extends Component {

  state = {
    loading: false,
  }

  componentDidMount() {
    this.wakeUpBackend();
  }

  wakeUpBackend = () => {
    this.setState({loading: true});
    axios.get('/up/')
      .then((response) => {
        this.setState({loading: false});
        console.log(response);
      })
      .catch((error) => {
        this.setState({loading: false});
        console.log(error);
        Modal.error({
          title: "Unable to reach server",
          content: "Unable to reach server. Please refresh page and try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  render() {
    if (!this.props.signedInUser) {
      return (
        <div className="HomeNoAuth">
          <h1>Welcome to Test Scoring</h1>
          <div align="center">
            { this.state.loading && <Spin size="large" />}
          </div>
          Sign in to access scoring tools.
          <br/>
          <br/>
          <Link to="/forgot">Forgot your password?</Link>
        </div>
      );
    }

    const startTests = this.props.assessments && this.props.assessments.map((assessment, index) =>
      <StartTest
        key={index}
        assessment={assessment}
      />
    );

    return (
      <div className="Home">
        <div className="HomeSearch">
          <Search/>
        </div>
        <div align="center">
          { this.state.loading && <Spin size="large" />}
        </div>
        <Row type="flex">
          {startTests}
        </Row>
      </div>
    );
  }
}

export default Home;
