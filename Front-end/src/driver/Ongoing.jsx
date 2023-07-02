import React from "react";
import { Breadcrumb } from "../components/Breadcrumb";
import { Table } from "@components/Table";
import { useNavigate } from "react-router-dom";
import { useData } from "../hooks/useData";
import { TableHolder } from "../components/TableHolder/TableHolder";

const ViewButton = ({ row }) => {
  const navigate = useNavigate();

  const id = row.values.rideId;
  return <button onClick={() => navigate(`/rides/${id}`)}>View</button>;
};

const COLUMNS = [
  {
    Header: "Ride ID",
    accessor: "rideId",
  },
  {
    Header: "Passenger",
    accessor: "passenger_name",
  },
  {
    Header: "From",
    accessor: "start_from",
  },
  {
    Header: "Destination",
    accessor: "destination",
  },
  {
    Header: "Start Time",
    accessor: (data) => {
      const date = new Date(data.requested_time);
      let time = date.toLocaleString("en-US", {
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      });
      return `${date.getDate()}/${date.getMonth()}/${date.getFullYear()} ${time}`;
    },
  },
  {
    Header: "Chance Pooled Rides",
    accessor: (data) => `50 %`,
  },
  {
    Header: "Expected Amount",
    accessor: (data) => <>&#8377; 1000</>,
  },
  {
    Header: "Status",
    accessor: "status",
  },
  {
    Header: "View",
    accessor: "view",
    Cell: ViewButton,
  },
];

export const Ongoing = () => {
  const { isLoading, error, data } = useData("ongoing_req", "api/ongoingrides");

  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;
  console.log(data);

  return (
    <div>
      <Breadcrumb />
      <TableHolder>
        <Table columns={COLUMNS} data={data} />
      </TableHolder>
    </div>
  );
};
