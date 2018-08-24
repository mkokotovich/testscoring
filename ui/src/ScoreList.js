import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Table } from 'antd';

import './ScoreList.css';

class ScoreList extends Component {

  expandedRowRender = (record) => {
    const related_items = this.props.test.items.filter(item => item.group === record.group);
    console.log("related" + related_items)
    return related_items.map(item =>
      <div key={item.number}>
        Item {item.number}{item.description ? ` (${item.description})` : ''}: {item.score}
      </div>
    );
  }
    
  render() {
    const columns = [
      {
        title: "Group",
        dataIndex: "group",
        key: "group",
        width: 200,
      },
      {
        title: "Raw Score",
        dataIndex: "score",
        key: "score",
      },
    ];

    return (
      <div className="ScoreList">
        <Table
          dataSource={this.props.scores}
          columns={columns}
          rowKey={score => score.group}
          pagination={false}
          size='middle'
          expandedRowRender={this.expandedRowRender}
          expandRowByClick={true}
        />
      </div>
    );
  }
}

export default withRouter(ScoreList);
