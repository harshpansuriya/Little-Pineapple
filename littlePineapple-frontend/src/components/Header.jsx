export default function Header() {
    return (
        <div className='flex justify-between border-b-4'>
            <div className='text-xl'>
                <p className='text-4xl font-bold'>Little Pineapple 🍍</p>
            </div>
            <div className='flex gap-4 '>
                <a href='/'>Home</a>
                <p>Skillers</p>
                <p>About</p>
                <p>Login</p>
                <p>Register</p>
            </div>
        </div>
    )
}