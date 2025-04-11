import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Modal, Spin } from 'antd';
import axios from 'axios';
import ScoreList from './ScoreList';
import './TestScores.css';

function TestScores(props) {
  const [testScores, setTestScores] = useState({});
  const [loading, setLoading] = useState(false);
  const { testId } = useParams();

  useEffect(() => {
    setTestScores({});
    loadScores();
  }, [testId]);

  const loadScores = () => {
    setLoading(true);
    axios.get(`/api/testing/v1/tests/${testId}/scores`)
      .then((response) => {
        console.log(response);
        setLoading(false);
        setTestScores(response.data);
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
        Modal.error({
          title: "Unable to load scores",
          content: "Unable to load scores:\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  return (
    <div className="TestScores">
    { testScores.test && <h2>Scores for {testScores.test.test_type} for client {testScores.test.client_number}</h2> }
    <div align="center">
    { loading && <Spin size="large" />}
      </div>

      { testScores.test && testScores.test.created_with_reverse_scoring  &&
        <>
        <div className="ReverseScoringWarning">
        🚨 Reverse Scoring Used 🚨
        </div>
        <p>This test includes items that use reverse scoring, but the
        software reversed the scores automatically. Item scores in the
        expanded group view will represent what was entered, not the
        reverse scores used to calculate scores.
        </p>
        </>
      }

      <ScoreList scores={testScores.scores} test={testScores.test} />
      </div>
  );
}

export default TestScores;
