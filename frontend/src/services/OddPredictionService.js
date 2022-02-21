import axios from "axios";

const API_SERVER_URI = process.env.VUE_APP_API_SERVER_URI;

const apiClient = axios.create({
  baseURL: API_SERVER_URI,
  withCredentials: false,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export function getOdds(information){
    return apiClient.post("/api/compute_odds", information);
};
