import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Row, Col, Popconfirm } from 'antd';
import './Test.css';
import * as moment from 'moment';

function Test(props) {
  const archiveRestoreButton = !props.test.is_archived ? (
    <Button onClick={() => props.handleArchive(props.test.id)}>Archive</Button>
  ) : (
    <Button type="primary" onClick={() => props.handleRestore(props.test.id)}>Restore</Button>
  );

  return (
    <div className="Test">
      <Row type="flex" align="middle">
        <Col className="TestTitle TestDetail" xs={6} sm={6} md={3} >
          <Link to={{ pathname: `/tests/${props.test.id}/view` }} > Test {props.test.id}</Link>
        </Col>
        <Col className="TestDetail" xs={10} sm={10} md={4} lg={2} >
          <Link to={`/tests/?type=${props.test.test_type}`}>
            {props.assessmentBySlug[props.test.test_type]}
          </Link>
        </Col>
        <Col className="TestDetail" xs={8} sm={8} md={3} lg={2} >
          <Link to={`/tests/?clientid=${props.test.client_number}`}>
            Client {props.test.client_number}
          </Link>
        </Col>
        <Col className="TestDetail" xs={5} sm={5} md={2} >
          <Link to={{ pathname: `/tests/${props.test.id}/verify` }} > <Button disabled={props.test.is_archived}>Verify</Button> </Link>
        </Col>
        <Col className="TestDetail" xs={5} sm={5} md={2} >
          <Link to={{ pathname: `/tests/${props.test.id}/scores` }} > <Button>Scores</Button> </Link>
        </Col>
        <Col className="TestDetail" xs={5} sm={5} md={2} >
          <Link to={{ pathname: `/tests/${props.test.id}/edit` }} > <Button disabled={props.test.is_archived}>Edit</Button> </Link>
        </Col>
        <Col className="TestDetail" xs={9} sm={9} md={{span: 3, push: 5}} lg={{span: 5, push: 5}} >
          <div style={{"float": "right"}}>
            <div style={{display: "inlineBlock"}}>
              { archiveRestoreButton }
              &nbsp;
              <Popconfirm title="Really Delete?" onConfirm={() => props.handleDelete(props.test.id) }>
                <Button type="danger">Delete</Button>
              </Popconfirm>
            </div>
          </div>
        </Col>
        <Col className="TestDetail" xs={24} md={{span: 5, pull: 3}} lg={{span: 5, pull: 5}} >
          Created: {moment(props.test.created_at).calendar()}
        </Col>
      </Row>
    </div>
  );
}

export default Test;
