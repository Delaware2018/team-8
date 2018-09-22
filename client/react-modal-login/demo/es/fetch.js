import React, { Component } from 'react';


class Fetcher extends Component {
  constructor(props) {
    super(props);

    this.state = {
      data: null,
    };
  }

  componentDidMount() {
    fetch('https://api.mydomain.com')
      .then(response => response.json())
      .then(data => this.setState({ data }));
  }

   render() {
    return <BookListing books={this.state.data} />;
  }
}
