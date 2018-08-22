import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col } from 'antd';
import './TestEdit.css';

class TestEdit extends Component {

  render() {
    const testId = this.props.match.params.testId;
    return (
      <div className="TestEdit">
        Edit test {testId}
      </div>
    );
  }
}

export default withRouter(TestEdit);
