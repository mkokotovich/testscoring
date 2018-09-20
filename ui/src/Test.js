import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Button, Row, Col, Popconfirm } from 'antd';
import './Test.css';
import * as moment from 'moment';
import { assessmentBySlug } from './Constants';

class Test extends Component {
  state = {
  }

  componentDidMount() {
  }

  render() {

    return (
      <div className="Test">
        <Row type="flex" align="middle">
          <Col className="TestTitle TestDetail" xs={6} sm={6} md={3} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/view` }} > Test {this.props.test.id}</Link>
          </Col>
          <Col className="TestDetail" xs={10} sm={10} md={4} >
            <Link to={`/tests/?type=${this.props.test.test_type}`}>
              {assessmentBySlug[this.props.test.test_type]}
            </Link>
          </Col>
          <Col className="TestDetail" xs={8} sm={8} md={3} >
            <Link to={`/tests/?clientid=${this.props.test.client_number}`}>
              Client {this.props.test.client_number}
            </Link>
          </Col>
          <Col className="TestDetail" xs={6} sm={6} md={2} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/verify` }} > Verify </Link>
          </Col>
          <Col className="TestDetail" xs={6} sm={6} md={2} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/scores` }} > Scores </Link>
          </Col>
          <Col className="TestDetail" xs={6} sm={6} md={2} >
            <Link to={{ pathname: `/tests/${this.props.test.id}/edit` }} > Edit </Link>
          </Col>
          <Col className="TestDetail" xs={6} sm={6} md={{span: 2, push: 6}} >
            <Popconfirm title="Really Delete?" onConfirm={() => this.props.handleDelete(this.props.test.id) }>
              <Button type="danger">Delete</Button>
            </Popconfirm>
          </Col>
          <Col className="TestDetail" xs={24} md={{span: 6, pull: 2}}>
            Created: {moment(this.props.test.created_at).calendar()}
          </Col>
        </Row>
      </div>
    );
  }
}

export default Test;
