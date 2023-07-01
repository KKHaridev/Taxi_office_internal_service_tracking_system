import React from "react";
import { Breadcrumb } from "@components/Breadcrumb";
import { Table } from "@components/Table";
import { useNavigate } from "react-router-dom";
import { useData } from "@hooks/useData";
import { TableHolder } from "@components/TableHolder/TableHolder";

const ViewButton = ({ row }) => {
  const navigate = useNavigate();

  const id = row.values.rideId;
  return (
    <button onClick={() => navigate(`/completed_rides/${id}`)}>View</button>
  );
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
    Header: "To",
    accessor: "destination",
  },
  {
    Header: "Start Time",
    accessor: "start_time",
  },
  {
    Header: "Expected Time",
    accessor: "expected_time",
  },
  {
    Header: "Chance Pooled Rides",
    accessor: (data) => `80 %`,
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

export const Completed = () => {
  const { isLoading, error, data } = useData("completed_req", "api/received");

  if (isLoading) return "Loading...";

  if (error) return "An error has occurred: " + error.message;

  return (
    <div>
      <Breadcrumb />
      <TableHolder>
        <Table columns={COLUMNS} data={data} />
      </TableHolder>
    </div>
  );
};
