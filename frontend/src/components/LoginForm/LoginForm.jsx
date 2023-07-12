import React from 'react';

// Styles
import {
  Button,
  Form,
  FormGroup,
  Label,
  Input,
} from 'reactstrap';

export default function LoginForm() {

  const handleSubmit = () => {
    
    console.log('Login Form Submitted');
  }

  return (
    <main>
      <div>LoginFormComponent</div>
      <Form>
        <FormGroup>
          <Label for="email">Email</Label>
          <Input
            type="email"
            name="email"
          />
        </FormGroup>
      <Button color="primary" onClick={handleSubmit}>Login</Button>
      </Form>
    </main>
  );
}