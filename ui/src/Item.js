import React, { Component } from 'react';
import { withRouter, Route, Link } from 'react-router-dom';
import { Row, Col, Modal, Icon, Input } from 'antd';
import axios from 'axios';
import './Item.css';

class Item extends Component {
  state = {
    score: undefined,
    error: false,
    saving: false
  }

  componentDidMount() {
    const { score } = this.props.item;
    this.setState({ score });
  }

  onChangeItemScore = (e) => {
    console.log(this.props.item)
    this.setState({ score: e.target.value });
  }

  onBlurItemScore = (e) => {
    console.log(this.props.item)
    this.setState({
      score: e.target.value,
      saving: true,
      error: false,
    });
    var data = {
      'score': e.target.value
    }
    axios.patch(`/api/testing/v1/items/${this.props.item.id}/`, data)
      .then((response) => {
        console.log(response);
        this.setState({
          'error': false,
          'saving': false,
        });
      })
      .catch((error) => {
        console.log(error);
        this.setState({
          'error': true,
          'saving': false,
        });
        Modal.error({
          title: `Unable to save item ${this.props.item.number}`,
          content: `Unable to save item ${this.props.item.number}. Please try again\n\n` + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  render() {
    //const iconType = "exclamation-circle" ? 
    //const iconType = this.state.saved ? "check-circle-o" : (this.state.error ? "exclamation-circle"
    var icon = ('');
    if (this.state.saving) {
      icon = (<Icon type="loading" />);
    } else if (this.state.error) {
      icon = (<Icon type="exclamation-circle" style={{ color: 'rgb(255, 30, 30)' }} />);
    } else {
      // An invisible check, so we don't bounce around when adding the other icons
      icon = (<Icon type="check" style={{ color: 'rgba(0, 0, 0, 0)' }} />);
    }

    return (
      <div className="Item">
        <Row type="flex" align="middle">
          <Col>
            <Input
              suffix={icon}
              value={this.state.score}
              onChange={this.onChangeItemScore}
              onBlur={this.onBlurItemScore}
            />
          </Col>
          <Col className="itemDescription">
            {this.props.item.description}
          </Col>
        </Row>
      </div>
    );
  }
}

export default withRouter(Item);
