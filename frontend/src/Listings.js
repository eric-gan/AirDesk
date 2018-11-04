import React, { Component } from 'react';

class Listings extends Component {
  render() {
      const {image_url, price, reviews } = this.props;
    return (
      <div className="Listings">
        <h1>
          George's cozy den Perfect for studying!
        </h1>
        <ul>
          <li> <img src = {image_url} alt='Broken'/> </li>
          <li> Price: {price} </li>
          <li> Reviews: {reviews} </li>
        </ul>
      </div>
    );
  }
}

export default Listings;
