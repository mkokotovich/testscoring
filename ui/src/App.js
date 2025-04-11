import React, {Component} from 'react';
import { Route, Routes, Link } from 'react-router-dom';
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
import Admin from './Admin';

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

  componentDidMount() {
    this.retrieveTestTypes();
  }

  retrieveTestTypes = () => {
    axios.get('/api/testing/v1/tests/types/')
      .then((response) => {
        this.setState({
          assessments: response.data,
        });
        this.setAssessmentBySlug(response.data.reduce(
          (accumulator, currentValue, currentIndex, array) => {
            accumulator[currentValue.slug] = currentValue.name;
            return accumulator;
          }, {}));
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
        Modal.error({
          title: "Unable to retrieve list of tests",
          content: "Unable to retrieve list of tests. Please refresh page and try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
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
          <Col><SignIn handleAuthChange={this.handleAuthChange} /></Col>
        </Row>
        <Routes>

          <Route path="/" element={ <Home signedInUser={this.state.user} assessments={this.state.assessments}/>} />
          <Route path="/tests/:testId/view" element={ <TestEdit readonly={true}/> } />
          <Route path="/tests/:testId/verify" element={ <TestEdit verify={true}/> } />
          <Route path="/tests/:testId/edit" element={ <TestEdit/> } />
          <Route path="/tests/:testId/scores" element={ <TestScores/> } />
          <Route path="/tests" element={ <TestList assessmentBySlug={this.state.assessmentBySlug}/> } />
          <Route path="/profile/password" element={ <ChangePassword user={this.state.user}/> } />
          <Route path="/profile" element={ <Profile user={this.state.user}/> } />
          <Route path="/reset" element={ <ResetPassword/> } />
          <Route path="/forgot" element={ <ForgotPassword/> } />
          <Route path="/admin" element={ <Admin user={this.state.user}/> } />
        </Routes>
      </div>
    );
  }
}

export default App;
