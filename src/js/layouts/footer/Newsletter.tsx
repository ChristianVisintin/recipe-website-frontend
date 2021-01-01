import React from "react";
import { Container, Col, Image, Row } from "react-bootstrap";
import styled from "styled-components";

import NewsletterForm from "./NewsletterForm";

//Logos
import Facebook from "../../../../assets/images/icons/facebook.svg";
import Instagram from "../../../../assets/images/icons/instagram.svg";
import Linkedin from "../../../../assets/images/icons/linkedin.svg";
import Github from "../../../../assets/images/icons/github.svg";

const Header = styled.h1`
  font-size: 1.2em;
  text-transform: uppercase;
`;

const SocialImage = styled(Image)`
  margin-right: 0.7em;
`;

export default function Newsletter() {
  return (
    <Container>
      <Row>
        <Col className="d-none d-md-block">
          <Header>Newsletter</Header>
        </Col>
      </Row>
      <Row>
        <Col className="d-none d-md-block">
          <NewsletterForm />
        </Col>
      </Row>
      <Row>
        <Col>
          <a href="https://github.com/ChristianVisintin/react-experiments">
            <SocialImage width="48" height="48" src={Facebook} />
          </a>
          <a href="https://github.com/ChristianVisintin/react-experiments">
            <SocialImage width="48" height="48" src={Instagram} />
          </a>
          <a href="https://www.linkedin.com/in/christian-visintin/">
            <SocialImage width="48" height="48" src={Linkedin} />
          </a>
          <a href="https://github.com/ChristianVisintin">
            <SocialImage width="48" height="48" src={Github} />
          </a>
        </Col>
      </Row>
    </Container>
  );
}