import { useMutation, useQuery } from "react-query";

const fetchData = (path) => {
  return fetch(`http://localhost:3000/${path}`).then((res) => res.json());
};

export const useData = (key, path, onSuccess, onError) => {
  return useQuery(key, () => fetchData(path), {
    onSuccess,
    onError,
    refetchInterval:1000
  });
};



const patchReq = ({id, data}) => {
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
export const useAcceptRide = () => {
  return useMutation(patchReq);
};
