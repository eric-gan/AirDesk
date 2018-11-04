import React, { Component } from 'react';
import './App.css';
import Listings from './Listings';
import SearchBar from './SearchBar';

class App extends Component {
  render() {
    return (
      <div className="App">
        <SearchBar />
        < Listings 
        image_url = {
            'http://www.returnofkings.com/wp-content/uploads/2014/10/study-den.jpg'
          }
        price = {'$294'}  
        reviews = {'4.9/5'}
        />
      </div>
    );
  }
}

export default App;
