import React, { Component } from 'react';
import './Heading.css';
// import GoogleMaps from './GoogleMaps';
import MapContainer from './MapContainer';
import MapWrapper from './MapWrapper';

class Heading extends Component {
  render() {
    return (
      <div className="HeaderContainer">
        <MapWrapper/>
      </div>
    );
  }
}

export default Heading;

