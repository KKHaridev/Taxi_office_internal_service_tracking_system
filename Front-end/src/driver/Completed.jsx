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
    accessor: (data) => {
      const date = new Date(data.starting_time);
      let time = date.toLocaleString("en-US", {
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      });
      if (data.starting_time != null) {
        return `${date.getDate()}/${date.getMonth()}/${date.getFullYear()} ${time}`;
      } else {
        return "-";
      }
    },
  },
  {
    Header: "Reached Time",
    accessor: (data) => {
      const date = new Date(data.reachedtime);
      let time = date.toLocaleString("en-US", {
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      });
      if (data.reachedtime != null) {
        return `${date.getDate()}/${date.getMonth()}/${date.getFullYear()} ${time}`;
      } else {
        return "-";
      }
    },
  },
  {
    Header: "Chance Pooled Rides",
    accessor: (data) => `${data.carpoolPercent} %`,
  },
  {
    Header: "Expected Amount",
    accessor: (data) => <>&#8377; {data.expectedDriverPay}</>,
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
  const { isLoading, error, data } = useData("completed_req", "api/completedrides");

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
