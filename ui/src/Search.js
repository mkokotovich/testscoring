import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Input, Button } from 'antd';
import './Search.css';

class Search extends Component {
  state = {
  }

  componentDidMount() {
  }

  searchByID(value) {
    this.props.history.push(`/tests/?search=${value}`);
  }

  viewAll = () => {
    this.props.history.push(`/tests/`);
  }

  render() {

    return (
      <div className="Search" style={{ marginBottom: 5}}>
        <Input.Search
          placeholder="Search by Client ID"
          enterButton="Search"
          style={{ width: 250 }}
          onSearch={value => this.searchByID(value)}
        />
        <Button style={{ marginLeft: 5 }} onClick={this.viewAll} >All Tests</Button>
      </div>
    );
  }
}

export default withRouter(Search);
