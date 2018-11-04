import React, { Component } from 'react';

import { Map, Marker, GoogleApiWrapper} from 'google-maps-react';

import styles from './styles.module.css';

class Contents extends Component {
  state = {
    position: null
  };

  componentDidMount() {
    this.renderAutoComplete();
  }

  componentDidUpdate(prevProps) {
    if (this.props !== prevProps.map) this.renderAutoComplete();
  }

  onSubmit(e) {
    e.preventDefault();
  }

  renderAutoComplete() {
    const { google, map } = this.props;

    if (!google || !map) return;

    const autocomplete = new google.maps.places.Autocomplete(this.autocomplete);
    autocomplete.bindTo('bounds', map);

    autocomplete.addListener('place_changed', () => {
      const place = autocomplete.getPlace();

      if (!place.geometry) return;

      if (place.geometry.viewport) map.fitBounds(place.geometry.viewport);
      else {
        map.setCenter(place.geometry.location);
        map.setZoom(17);
      }

      this.setState({ position: place.geometry.location });
    });
  }

  render() {
    const { position } = this.state;

    return (
      <div className={styles.flexWrapper}>
        <div className={styles.left}>
          <form onSubmit={this.onSubmit}>
            <input
              className={styles.searchBar}
              placeholder="Enter a location"
              ref={ref => (this.autocomplete = ref)}
              type="text"
            />

            <input className={styles.searchBarButton} type="submit" value="Go" />
          </form>
        </div>

        <div className={styles.right}>
          <Map
            {...this.props}
            center={position}
            centerAroundCurrentLocation={true}
            containerStyle={{
              height: '500px',
              position: 'relative',
              width: '700px'

            }}>
            <Marker position={position} />
          </Map>
        </div>
      </div>
    );
  }
}

const MapWrapper = props => (
  <Map className="map" google={props.google} visible={false}>
    <Contents {...props} />
  </Map>
);

export default GoogleApiWrapper({
  apiKey: ('AIzaSyB0mxT2fWkC1tsdGcxD5_rWpLxPsHoKEVQ')
})(MapWrapper)

          // <div>
          //   <div>Lat: {position && position.lat()}</div>
          //   <div>Lng: {position && position.lng()}</div>
          // </div>