import React, { Component } from 'react';
import './App.css';
import Heading from './Heading';
import AllListings from './AllListings';

class App extends Component {

  render() {
    return (
      <div className="App">
        <Heading/>
        <AllListings
        />
      </div>
    );
  }
}

export default App;
