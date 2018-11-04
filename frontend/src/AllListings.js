import React, { Component } from 'react';
import './AllListings.css';
import Listings from './Listings';

class AllListings extends Component {
  render() {
    const properties = [1,2,3];
    // const { properties } = this.props;
    return (
      <div className="AllListings">
        {
          properties.map(property => {
            return ( 
              <div className="IndividualListing">
                <Listings 
                  image_url = {
                      'http://www.returnofkings.com/wp-content/uploads/2014/10/study-den.jpg'
                    }
                  price = {'$294'}  
                  reviews = {'4.9/5'}
                /> 
              </div>
            )
          })
        }
      </div>
    );
  }
}

export default AllListings;
