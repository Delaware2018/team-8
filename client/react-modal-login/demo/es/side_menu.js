import React from "react";
import { slide as Menu } from "react-burger-menu";

export default props => {
  return (
    // Pass on our props
    <Menu {...props}>
      <a className="menu-item" href="/">
      <br></br>
        Wallet
      </a>

      <a className="menu-item" href="/">
        Home
      </a>

      <a className="menu-item" href="/leaderboard">
        Leaderboard
      </a>

      <a className="menu-item" href="/something">
        Something
      </a>

      <a className="menu-item" href="https://bepositive.org/">
        Be Positive
      </a>
    </Menu>
  );
};
