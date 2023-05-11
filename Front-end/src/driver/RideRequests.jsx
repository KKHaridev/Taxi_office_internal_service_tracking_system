import React from "react";
import { Breadcrumb } from "../components/Breadcrumb";
import { Table } from "@components/Table";
import { useQuery } from "react-query";
import { useNavigate } from "react-router-dom";
import { useAcceptRide, useData } from "../hooks/useData";
import { Modal } from "../components/Modals/Modal";
import { CloseIcon, CheckIcon } from "@chakra-ui/icons";
import { TableHolder } from "../components/TableHolder/TableHolder";

const ViewButton = ({ row }) => {
  const navigate = useNavigate();

  const id = row.values.id;
  return (
    <button onClick={() => navigate(`/received_rides/${id}`)}>View</button>
  );
};

const Accept_Reject = ({ row }) => {
  const id = row.values.id;
  const status = row.values.status;
  const { mutate } = useAcceptRide();

  return status == "accepted" ? (
    "-"
  ) : (
    <>
      <Modal
        title="Accept"
        color="#EA0000"
        hColor="#FB4C4C"
        handler={() => {
          const data = { status: "cancelled" };
          mutate({ id, data });
        }}
      >
        <CloseIcon color="brand.red" />
      </Modal>
      <Modal
        title="Accept"
        color="#6E2594"
        hColor="#8344a5"
        handler={() => {
          const data = { status: "accepted" };
          mutate({ id, data });
        }}
      >
        <CheckIcon color="brand.green" />
      </Modal>
    </>
  );
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
    Header: "Accept/Reject",
    accessor: "accet_or_reject",
    Cell: Accept_Reject,
  },
  {
    Header: "View",
    accessor: "view",
    Cell: ViewButton,
  },
];

export const RideRequests = () => {
  const { isLoading, error, data } = useData(
    "req_rides",
    "req_rides?driverId=1&status=pending&status=accepted"
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
