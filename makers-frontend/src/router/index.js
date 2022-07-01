import Vue from "vue";
import VueRouter from "vue-router";
const LandingPage = () => import("./../views/LandingPage");

Vue.use(VueRouter);

const routes = [{ path: "/", name: "LandingPage", component: LandingPage }];

const router = new VueRouter({
	routes,
});

export default router;
