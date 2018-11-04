import React, { Component } from 'react';
import './App.css';
import AllListings from './AllListings';

import SearchBar from './SearchBar';

class App extends Component {

  render() {
    return (
      <div className="App">
        <SearchBar />
        <AllListings
        />
      </div>
    );
  }
}

export default App;
