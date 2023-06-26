import { useMutation, useQuery } from "react-query";

const fetchData = (path) => {
  return fetch(`http://localhost:3000/${path}`).then((res) => res.json());
};

export const useData = (key, path, options = {}) => {
  return useQuery(key, () => fetchData(path), {
    ...options,
  });
};

const fetchData1 = (path) => {
  return fetch(`http://127.0.0.1:8000/${path}`).then((res) => res.json());
};

export const useData1 = (key, path, options = {}) => {
  return useQuery(key, () => fetchData1(path), {
    ...options,
  });
};

const patchReq = ({ id, data }) => {
  return fetch(`http://localhost:3000/req_rides/${id}`, {
    method: "PATCH",
    body: JSON.stringify(data),

    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
};

const updateStatus = ({ id, data }) => {
  return fetch(`http://localhost:3000/drivers/${id}`, {
    method: "PATCH",
    body: JSON.stringify(data),

    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
};

const deleteUser = ({ id }) => {
  return fetch(`http://localhost:3000/drivers/${id}`, {
    method: "DELETE",

    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
};

const createDriver = async (data) => {
  return await fetch(`http://localhost:3000/drivers/`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
};

export const useAcceptRide = () => {
  return useMutation(patchReq);
};

export const useDelete = () => {
  return useMutation(deleteUser);
};

export const useUpdateStatus = () => {
  return useMutation(updateStatus);
};

export const useCreateDriver = () => {
  return useMutation(createDriver);
};
