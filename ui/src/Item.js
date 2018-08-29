import React, { Component } from 'react';
import { Button, Row, Col, Modal, Icon, Input } from 'antd';
import axios from 'axios';
import './Item.css';

class Item extends Component {
  state = {
    score: undefined,
    verifiedScore: undefined,
    error: false,
    conflict: false,
    saving: false
  }

  componentDidMount() {
    const { score } = this.props.item;
    this.setState({ score });
  }

  resolveConflict = () => {
    this.updateItem(this.state.verifiedScore);
    this.setState({
      conflict: false,
      score: this.state.verifiedScore
    });
    this.props.updateConflicts(this.props.item.number, false);
  }

  onChangeItemsVerify = (e) => {
    console.log(this.props.item)
    this.setState({ verifiedScore: e.target.value },
      () => {
        if (this.state.verifiedScore.length >= 1) {
          const conflict = this.state.verifiedScore !== this.state.score;
          this.setState({ conflict });
          this.props.updateConflicts(this.props.item.number, conflict);
          this.props.changeFocus(this.props.index);
        }
      }
    );
  }

  onChangeItemScore = (e) => {
    console.log(this.props.item)
    this.setState({ score: e.target.value },
      () => {
        if (this.state.score.length >= 1) {
          this.updateItem(this.state.score);
          this.props.changeFocus(this.props.index);
        }
      }
    );
  }

  updateItem = (score) => {
    this.setState({
      score: score,
      saving: true,
      error: false,
    });
    var data = {
      'score': score
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
    var icon = ('');
    if (this.state.saving) {
      icon = (<Icon type="loading" />);
    } else if (this.state.error || this.state.conflict) {
      icon = (<Icon type="exclamation-circle" style={{ color: 'rgb(255, 30, 30)' }} />);
    } else {
      // An invisible check, so we don't bounce around when adding the other icons
      icon = (<Icon type="check" style={{ color: 'rgba(0, 0, 0, 0)' }} />);
    }

    const changeCallback = this.props.verify ? this.onChangeItemsVerify : this.onChangeItemScore;
    const inputValue = this.props.verify? this.state.verifiedScore : this.state.score;

    return (
      <div className="Item">
        <Row type="flex" align="middle">
          <Col>
            <Input
              ref={this.props.inputRef}
              suffix={icon}
              value={inputValue}
              onChange={changeCallback}
              disabled={this.props.readonly}
            />
          </Col>
          <Col className="itemDescription">
            Item {this.props.item.number}
          </Col>
          { this.state.conflict ?
            <Col>
              <Button type="danger" className="conflictButton" onClick={this.resolveConflict}>Resolve Inconsistency</Button>
            </Col> : ''
          }
        </Row>
      </div>
    );
  }
}

export default Item;
