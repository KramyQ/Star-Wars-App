import { createRouter, createWebHistory } from "vue-router";
import InformantSection from "../views/InformantSection.vue";
import Bar from "../views/Bar.vue";

const routes = [
  {
    path: "/InformantSection",
    name: "InformantSection",
    component: InformantSection,
  },
  {
    path: "/Bar",
    name: "Bar",
    component: Bar,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
