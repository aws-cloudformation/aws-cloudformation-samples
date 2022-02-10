package com.awssamples.sqspolicyencryption.hook;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.Map;
import java.util.List;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode(callSuper = false)
@ToString
@JsonAutoDetect(fieldVisibility = Visibility.ANY, getterVisibility = Visibility.NONE, setterVisibility = Visibility.NONE)
public class Policy {
    @JsonIgnore
    public static final String TYPE_NAME = "AWS::IAM::Policy";

    @JsonIgnore
    public static final String IDENTIFIER_KEY_ID = "/properties/Id";

    @JsonProperty("Id")
    private String id;

    @JsonProperty("Groups")
    private List<String> groups;

    @JsonProperty("PolicyDocument")
    private Map<String, Object> policyDocument;

    @JsonProperty("PolicyName")
    private String policyName;

    @JsonProperty("Roles")
    private List<String> roles;

    @JsonProperty("Users")
    private List<String> users;
}
