import Layout from "@/Layout/index";
import Home from "@/views/Home";
import TaskList from "@/views/TaskList";
import UserList from "@/views/UserList";
import UserInfo from "@/views/UserInfo";

export default {
  routes: [
    {
      path: "/",
      component: Layout,
      children: [
        { path: "", component: Home },
        { path: "/tasklist", component: TaskList },
        { path: "/userList", component: UserList },
        { path: "/userInfo", component: UserInfo },
      ],
    },
  ],
};