import React from "react";
import { Breadcrumb } from "../components/Breadcrumb";
import { Table } from "@components/Table";
import { useNavigate } from "react-router-dom";
import { useData } from "../hooks/useData";
import { TableHolder } from "../components/TableHolder/TableHolder";

const ViewButton = ({ row }) => {
  const navigate = useNavigate();

  const id = row.values.id;
  return <button onClick={() => navigate(`/ongoing_rides/${id}`)}>View</button>;
};

const COLUMNS = [
  {
    Header: "Ride ID",
    accessor: "id",
  },
  {
    Header: "Passenger",
    accessor: "pass_name",
  },
  {
    Header: "From",
    accessor: "from",
  },
  {
    Header: "To",
    accessor: "to",
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
    accessor: (data) => `${data.percentage} %`,
  },
  {
    Header: "Expected Amount",
    accessor: (data) => <>&#8377; {data.exp_amount}</>,
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
  const { isLoading, error, data } = useData(
    "ongoing_req",
    "req_rides?driverId=1&status_ne=pending&status_ne=canceled&status_ne=reached"
  );

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
