import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';
import { Row, Col, Modal, Spin } from 'antd';
import StartTest from './StartTest';
import axios from 'axios';
import './Home.css';

class Home extends Component {

  assessments = [
    {
      slug: "cbcl_6_18",
      name: "CBCL 6-18"
    },
    {
      slug: "cbcl_1_5",
      name: "CBCL 1.5-5"
    },
    {
      slug: "conners3_parent",
      name: "Conners 3 - Parent"
    },
    {
      slug: "tscyc",
      name: "TSCYC"
    },
    {
      slug: "brief2",
      name: "BRIEF2"
    },
    {
      slug: "srs2",
      name: "SRS2"
    },
    {
      slug: "scared",
      name: "SCARED"
    },
    {
      slug: "tscc",
      name: "TSCC"
    }
  ]


  state = {
    loading: false
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
      const listOfTests = this.assessments.map((assessment, index) =>
        <li>{assessment.name}</li>
      );

      return (
        <div className="Home">
          <h1>Welcome to Test Scoring</h1>
          <div align="center">
            { this.state.loading && <Spin size="large" />}
          </div>
          Sign in to access scoring tools for the following tests:
          <ul>
            { listOfTests }
          </ul>
          <br/>
          <Link to="/forgot">Forgot your password?</Link>
        </div>
      );
    }

    const startTests = this.assessments.map((assessment, index) =>
      <StartTest
        key={index}
        assessment={assessment}
      />
    );

    return (
      <div className="Home">
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

export default withRouter(Home);
