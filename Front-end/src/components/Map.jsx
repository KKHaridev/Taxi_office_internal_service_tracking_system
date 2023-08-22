import React from "react";
import { MapContainer, TileLayer, Marker } from "react-leaflet";
import MarkerClusterGroup from "react-leaflet-cluster";
import MapFullScreen from "./MapFullScreen";

export const addressPoints = [
  [40.780078358949893, -73.960673974467397],
  [40.646255785919898, -73.784883206389665],
  [40.770169181619735, -73.872255906701724],
  [40.725767414067676, -73.996344250052076],
  [40.755507681362332, -73.982438718280932],
];

export const MapWrapper = ({ height }) => {
  return (
    <MapContainer
      center={[addressPoints[1][0], addressPoints[1][1]]}
      zoom={10}
      style={{ width: "100%", height: height, zIndex: 10 }}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <MarkerClusterGroup>
        {addressPoints.map((marker, index) => (
          <Marker key={index} position={[marker[0], marker[1]]} />
        ))}
      </MarkerClusterGroup>
    </MapContainer>
  );
};

const Map = ({ height }) => {
  return (
    <>
      <MapFullScreen />
      <MapWrapper height={height} />
    </>
  );
};

export default Map;
