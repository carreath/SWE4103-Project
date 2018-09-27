import axios from 'axios'

export default() => {
    // TODO - Will have to update the base baseURL once we get a working backend
    return axios.create({
        baseURL: ``,
        withCredentials: false,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
}
