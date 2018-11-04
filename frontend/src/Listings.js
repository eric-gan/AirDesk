import React, { Component } from 'react';
import './Listings.css';

class Listings extends Component {
  render() {
      const {image_url, price, reviews } = this.props;
    return (
      <div className="ListingsContainer">
        <div className="ListingImageContainer">
          <img src = {image_url} alt='Broken' className="ListingImage"/>
        </div>
        <div className="ListingContent">
          <h2 className="ListingContentType">
            George's cozy den Perfect for studying!
          </h2>
          <h1 className="ListingContentTitle">
            Large private bedroom
          </h1>
          <p>Amenities here!</p>
        </div>
        <div className="ListingPrice">
          <p> Price: {price} </p>
          <p> Reviews: {reviews} </p>
        </div>
      </div>
    );
  }
}

export default Listings;
