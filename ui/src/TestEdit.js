import React, { useState, useEffect } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import { Modal, Spin, Affix, Button } from 'antd';
import axios from 'axios';
import ItemList from './ItemList';
import './TestEdit.css';

function TestEdit(props) {
  const [test, setTest] = useState({});
  const [readonly, setReadonly] = useState(false);
  const [loading, setLoading] = useState(false);
  const [allVerified, setAllVerified] = useState(false);
  const [inconsistencies, setInconsistencies] = useState([]);
  const [conflicts, setConflicts] = useState({});
  const { testId } = useParams();
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    loadTest();
    if (location.state) {
      const {locReadonly} = location.state
      if (locReadonly) {
        setReadonly(locReadonly);
      }
    }
  }, [location.state]);

  useEffect(() => {
    if (props.readonly !== undefined) {
      setReadonly(props.readonly);
    }
  }, [props.readonly]);

  useEffect(() => {
    setTest([]);
    loadTest();
  }, [testId]);

  const loadTest = () => {
    setLoading(true);
    axios.get(`/api/testing/v1/tests/${testId}/`)
      .then((response) => {
        console.log(response);
        setLoading(false);
        setTest(response.data);
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
        Modal.error({
          title: "Unable to load test",
          content: "Unable to load test. Please try again\n\n" + error + "\n\n" + JSON.stringify(error.response.data),
          maskClosable: true,
        })
      });
  }

  const updateConflicts = (itemId, conflict) => {
    var newConflicts = conflicts;
    newConflicts[itemId] = conflict;
    setConflicts(newConflicts);
    setAllVerified(test.items ? Object.keys(newConflicts).length === test.items.length : false);
    setInconsistencies(Object.keys(newConflicts).reduce((filtered, key) => {
        if (newConflicts[key]) {
          filtered.push(key);
        }
        return filtered;
      }, [])
    )
  }

  const handleEdit = () => {
    navigate(`/tests/${testId}/edit`);
  }

  const handleVerify = () => {
    navigate(`/tests/${testId}/verify`);
  }

  const handleViewInconsistencies = () => {
    const onlyErrors = Object.keys(conflicts).reduce((filtered, key) => {
      if (conflicts[key]) {
        filtered.push(key);
      }
      return filtered;
    }, []);
    if (onlyErrors.length > 0) {
      Modal.error({
        title: "Inconsistencies Found",
        content: "Inconsistencies found in items " + onlyErrors.join(", "),
        maskClosable: true,
      })
    }
  }

  const handleViewScores = () => {
    navigate(`/tests/${testId}/scores`)
  }

  const verb = props.readonly ? "Viewing" : props.verify ? "Verifying" : "Editing";

  return (
    <div className="TestEdit">
      <h2>{verb} {test.test_type} for client {test.client_number}</h2>
      <div align="center">
        { loading && <Spin size="large" />}
      </div>

      <Affix>
        <div className="AlignRight">
          { readonly ? 
            <Button
              className="TopRightButton"
              onClick={handleEdit}>
                Edit
            </Button> : '' 
          }
          { props.verify ? (
            <React.Fragment>
            { inconsistencies.length > 0 ? 
              <Button
                className="TopRightButton"
                onClick={handleViewInconsistencies}>
                  View Inconsistencies
              </Button> : ''
            }
            {
              allVerified && inconsistencies.length === 0 ? 
              <Button
                className="TopRightButton"
                onClick={handleViewScores}>
                  View Scores
              </Button> : ''
            }
            </React.Fragment>
          ) :
            <React.Fragment>
              <Button
                className="TopRightButton"
                onClick={handleVerify}>
                  Verify
              </Button>
              <Button
                className="TopRightButton"
                onClick={handleViewScores}>
                  View Scores
              </Button>
            </React.Fragment>
          }
        </div>
      </Affix>

      { test.created_with_reverse_scoring  &&
        <>
          <div className="ReverseScoringWarning">
            🚨 Reverse Scoring 🚨
          </div>
          <p>This test includes items that use reverse scoring, but the
          software will reverse it for you. Please enter the scores without
          reversing any numbers.
          </p>
        </>
      }

      <ItemList
        items={test.items}
        readonly={readonly}
        verify={props.verify}
        updateConflicts={updateConflicts}
      />
    </div>
  );
}

export default TestEdit;
