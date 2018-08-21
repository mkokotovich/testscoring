import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col } from 'antd';
import './CBCLEdit.css';

class CBCLEdit extends Component {

  render() {
    const testId = this.props.match.params.testId;
    return (
      <div className="CBCLEdit">
        Edit test {testId}
      </div>
    );
  }
}

export default withRouter(CBCLEdit);
