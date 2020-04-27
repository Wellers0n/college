import React from 'react';
import styled from 'styled-components'
import { space, width, fontSize, color, height } from 'styled-system';

const Img = styled.img`
  ${width}
`;

const Center = styled.div`
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Root = styled.div([], {
    width: '50vw',
    height: '100vh',
    display: 'flex',
    
});

const Title = styled.span`
  font-size: 50px;
  ${space}
`;


const ImgCenter = styled.div`
  display: flex;
  flex-direction: column;
`
const Link = styled.a`
    color: #6CDAFB;

`


export const Slack = () => (
  <Root>
    <Center>
      <Title mb={'15%'}>Join Slack</Title>
      <ImgCenter>
        <Img src={"./img/reactBR.png"} width={width}/>
        <Link href="https://react-brasil-slack.herokuapp.com/">React Brasil</Link>
      </ImgCenter>
    </Center>
  </Root>
);
