class Wishlist extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            wishlist: null,

          }
    }
    componentDidMount() {
        $.get('/api/wishlist', (wishlist) => {
            this.setState({ wishlist: wishlist,
                            completed: completed
            });
          });
    }

    render() { 
        // if this.state.wishlist, display wishlist
        let display = null;

        if (!this.state.wishlist){
            display = 
            <div id="add_to_wishlist">
                <form action="" method="post">
                <label for="wishlist">Add to Wishlist:</label>
                <textarea id="wishlist" name="wishlist" 
                                rows="10" 
                                cols="60"
                                maxlength='1000'
                                minlegth='5'
                                placeholder="Add to wishlist.."
                                ></textarea>
                <input type="submit"></input>
                </form>
            </div>
        } else {
            display = 
            <h3>
            {this.state.wishlist}
            </h3>
        }
        
        
        
        return ( 
            <div>
                {display}
                <p>JSX!</p>
            </div>
         );
    }
}
 

ReactDOM.render(<Wishlist />, document.querySelector('#wishlist'));