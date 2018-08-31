import React, { Component } from 'react';
import { Route, Link } from 'react-router-dom';
import { Row, Col } from 'antd';
import './App.css';
import SignIn from './SignIn';
import Home from './Home';
import TestEdit from './TestEdit';
import TestList from './TestList';
import TestScores from './TestScores';
import Profile from './Profile';

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
          <Col className="Logo"><Link to="/">Test Scoring</Link></Col>
          <Col><SignIn handleAuthChange={this.handleAuthChange} /></Col>
        </Row>
        <Route
          exact
          path="/"
          render={() => {
            return <Home signedInUser={this.state.user}/>;
          }}
        />
        <Route
          path={`/tests/:testId/view`}
          render={() => {
            return <TestEdit readonly={true}/>;
          }}
        />
        <Route
          path={`/tests/:testId/verify`}
          render={() => {
            return <TestEdit verify={true}/>;
          }}
        />
        <Route
          path={`/tests/:testId/edit`}
          render={() => {
            return <TestEdit/>;
          }}
        />
        <Route
          path={`/tests/:testId/scores`}
          render={() => {
            return <TestScores/>;
          }}
        />
        <Route exact path={`/tests/:testType`} component={TestList}/>
        <Route
          path={`/profile`}
          render={() => {
            return <Profile user={this.state.user}/>;
          }}
        />
      </div>
    );
  }
}

export default App;
